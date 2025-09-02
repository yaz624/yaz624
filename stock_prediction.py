# pip install yfinance

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import yfinance as yf
from datetime import datetime, timedelta
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np


def plot_growth_rates_and_predictions(historical_data, model, specific_date, period_in_days):
    try:
        specific_date = datetime.strptime(specific_date, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Invalid Date", "Invalid date format. Please use YYYY-MM-DD.")
        return

    specific_month_day = specific_date.strftime("%m-%d")
    matching_dates = historical_data.index[historical_data.index.strftime("%m-%d") == specific_month_day]

    if matching_dates.empty:
        messagebox.showinfo("No Data", f"No matching historical data found for {specific_month_day}.")
        return

    specific_date_mapped = matching_dates[-1]
    future_dates = [specific_date_mapped + timedelta(days=i) for i in range(1, period_in_days + 1)]
    future_data = historical_data[historical_data.index.isin(future_dates)]

    if future_data.empty:
        messagebox.showinfo("No Data", f"No data found for the next {period_in_days} days after {specific_date_mapped}.")
        return

    future_data.loc[:, 'Days'] = (future_data.index - specific_date_mapped).days
    X_future = future_data['Days'].values.reshape(-1, 1)
    y_future = future_data['Close'].values

    predicted_prices = model.predict(X_future)
    growth_rates = [(predicted_prices[i] - predicted_prices[i-1]) / predicted_prices[i-1] * 100 if i > 0 else 0 for i in range(len(predicted_prices))]

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=future_data.index, y=predicted_prices, mode='lines+markers', name='Predicted Prices', line=dict(color='orange', dash='dash')))
    fig1.update_layout(title=f"Predicted Stock Prices for the Next {period_in_days} Days (Mapped to {specific_date_mapped.date()})", xaxis_title="Date", yaxis_title="Stock Price ($)", hovermode="x unified", template="plotly_white")
    fig1.show()

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=future_data.index, y=growth_rates, mode='lines+markers', name='Growth Rates (%)', line=dict(color='green', dash='solid')))
    fig2.update_layout(title=f"Growth Rates for the Next {period_in_days} Days (Mapped to {specific_date_mapped.date()})", xaxis_title="Date", yaxis_title="Growth Rate (%)", hovermode="x unified", template="plotly_white")
    fig2.show()

    min_price_index = np.argmin(predicted_prices)
    max_price_index = np.argmax(predicted_prices)
    best_invest_day = future_data.index[min_price_index]
    best_withdraw_day = future_data.index[max_price_index]

    invest_growth_rate = growth_rates[min_price_index]
    withdraw_growth_rate = growth_rates[max_price_index]

    messagebox.showinfo("Investment Advice", f"Best Day to Invest: {best_invest_day.date()} - Price: ${predicted_prices[min_price_index]:.2f} (Growth: {invest_growth_rate:.2f}%)\n\nBest Day to Withdraw: {best_withdraw_day.date()} - Price: ${predicted_prices[max_price_index]:.2f} (Growth: {withdraw_growth_rate:.2f}%)")


def fetch_stock_analysis_gui():
    def fetch_data():
        company_symbol = symbol_entry.get().strip()
        company = yf.Ticker(company_symbol)

        try:
            company_info = company.info
            messagebox.showinfo("Company Info", f"Analyzing {company_info['shortName']} ({company_symbol})\nIndustry: {company_info.get('industry', 'N/A')}\nSector: {company_info.get('sector', 'N/A')}")
        except Exception as e:
            messagebox.showerror("Error", f"Unable to fetch company information. Please check the symbol.\n{e}")
            return

        choice = time_range_var.get()
        period_in_days = int(period_in_days_var.get())  # Get user input for the number of days ahead
        today = datetime.today()

        # Adjust start date based on user's selection
        if choice == "6 Months":
            start_date = today - timedelta(days=6 * 30)
        elif choice == "1 Year":
            start_date = today - timedelta(days=365)
        elif choice == "2 Years":
            start_date = today - timedelta(days=2 * 365)
        elif choice == "5 Years":
            start_date = today - timedelta(days=5 * 365)
        elif choice == "Custom Range":
            start_date = simpledialog.askstring("Custom Range", "Enter the start date (YYYY-MM-DD):").strip()
            try:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Invalid Date", "Invalid date format. Please use YYYY-MM-DD.")
                return
        else:
            messagebox.showerror("Invalid Choice", "Please select a valid option.")
            return

        try:
            historical_data = company.history(start=start_date, end=today)
            if historical_data.empty:
                messagebox.showinfo("No Data", "No data available for the selected date range.")
                return
        except Exception as e:
            messagebox.showerror("Error", f"Unable to fetch historical data.\n{e}")
            return

        historical_data.index = historical_data.index.tz_localize(None)
        historical_data['Days'] = (historical_data.index - historical_data.index.min()).days
        X = historical_data['Days'].values.reshape(-1, 1)
        y = historical_data['Close'].values

        model = LinearRegression()
        model.fit(X, y)
        r2_score = model.score(X, y)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=historical_data.index, y=historical_data['Close'], mode='lines', name='Historical Prices', line=dict(color='blue')))
        fig.update_layout(title=f"Stock Price Prediction for {company_symbol}", xaxis_title="Date", yaxis_title="Stock Price ($)", hovermode="x unified", template="plotly_white")
        fig.show()

        analyze_specific_date = messagebox.askyesno("Analyze Date", "Would you like to analyze a specific date for investment/withdrawal?")
        if analyze_specific_date:
            specific_date = simpledialog.askstring("Specific Date", "Enter the date (YYYY-MM-DD):").strip()
            plot_growth_rates_and_predictions(historical_data, model, specific_date, period_in_days)

    root = tk.Tk()
    root.title("Stock Market Risk Assessment Tool")

    tk.Label(root, text="Enter Stock Symbol:").grid(row=0, column=0, padx=10, pady=10)
    symbol_entry = tk.Entry(root)
    symbol_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Select Time Range:").grid(row=1, column=0, padx=10, pady=10)
    time_range_var = tk.StringVar(value="6 Months")
    time_ranges = ["6 Months", "1 Year", "2 Years", "5 Years", "Custom Range"]
    time_range_menu = tk.OptionMenu(root, time_range_var, *time_ranges)
    time_range_menu.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Select Period for Prediction (Days):").grid(row=2, column=0, padx=10, pady=10)
    period_in_days_var = tk.StringVar(value="15")
    period_in_days_menu = tk.OptionMenu(root, period_in_days_var, "15", "30", "90", "120", "150", "180")
    period_in_days_menu.grid(row=2, column=1, padx=10, pady=10)

    fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data, bg="orange", fg="white", font=("Helvetica", 14))
    fetch_button.grid(row=3, columnspan=2, pady=20)

    root.geometry("400x250")
    root.mainloop()


# Run the GUI-based stock analysis tool
fetch_stock_analysis_gui()
