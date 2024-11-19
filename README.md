                                        函数式编程:
I.definition：
函数式编程是一种编程范式programming paradigm 就是如何编写程序的方法论。
属于结构化编程的一种。 主要思想是把运算过程尽量写成一系列嵌套的函数调用
：（1+2）*3-4 to:
traditional: var a = 1+2; var b = a*3; var c = b - 4;
函数式编程要求使用函数， 把运算过程定义为不同的函数 写成：
    var result = subtract(multiply(add(1,2),3),4);
II.Feature:
1. 函数是first class， 指的是函数与其他数据类型一样，处于平等地位，可以赋值给其他变量，
   也可以作为参数，传入另一个函数，或作为别的函数的返回值。
2. 只用表达式，不用”语句“
   表达式expression 是一个单纯的运算过程，有返回值， 语句”statement“ 是执行某种操作
   没有返回值。 ”函数式编程要求只用表达式不用语句“ 每一步都是单纯运算且有返回值。
   函数式编程不考虑系统的I/O，是为了处理computation
3.没有函数内部与外部的互动（修改全局变量的值），产生运算以外的其他结果。
函数式编程没有“副作用” 意味着函数要保持独立，所有功能就是返回一个新的值，没有其他行为，
尤其是不得修改外部变量的值。
4.引用透明，不依赖于外部变量或状态，只依赖于输入的参数，任何时候只要参数相同，引用函数
所得到的返回值总是相同的。

III.Advantage:
1.代码简介，开发快速。
大量使用函数，减少了代码的重复，因此程序较短，开发速度较快。
2.接近自然语言，易于理解
自由度高，容易写出接近自然语言的代码。
For（1+2）*3-4
subtract(multiply(add(1,2),3),4)
变形：
add(1,2).multiply(3).subtract(4)
3.方便代码管理，

4.易于“并发编程”
函数式编程不需要考虑死锁，因为不修改变量，不存在锁线程的问题。
var s1 = 0p1();
var s2 = 0p2();
var s3 = concat(s1,s2);

                        Metaprogramming:
I. pros: abstraction in static languages
        code reuse
        limits human errors
II. cons:




    
