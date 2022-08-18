# 方針の立て方
$1≤Q≤2×10^5$, $1≤N≤2×10^5$なので、計算量的には$O(Q×1)$かO$(Q×logN)$あたりになると予想できる。

配列に対してのswap、rotation、値の取得の操作が$O(1)$または$O(logN)$で行える必要がある。

通常のListでは、値の取得は$O(1)$。おそらくswapも同様の速さで可能。あとはrotationを早くできれば間に合う。
普通に行うと、末尾をpop($O(1)$)して、先頭にinsert($O(n)$)する必要があり、これだと間に合わない。

rotationが早い($O(k)$なので、1つずらすだけなら$O(1)$)のはdequeだが、値の取得に($O(n)$)かかってしまう。

そこで、結局、listのrotationを早くするため、実際には配列をいじらずに、いくつずらしたかを変数として持っておき、swapや値の取得の際には、indexからそれを引く形で実装を行う。こうすることで、rotationが($O(1)$)で可能になる。
PyPy: 704 ms, 104116 KB
Python: 901 ms, 31000 KB

## （参考1）計算量系の話がまとまっている記事
[計算量のはなし](https://cppx.hatenablog.com/entry/2017/08/06/104144)

[競技プログラミングで解法を思いつくための典型的な考え方](https://algo-logic.info/how-to-think-cp/)

[AtCoder 計算量について学ぶ](https://syachineko.hatenablog.com/entry/2020/09/10/224757)


## （参考2）PythonのList, deque, set, dictなどの計算量の話がまとまっている記事
[Pythonの計算量の話](https://jp.magicode.io/goregraind/articles/9dce106e24e64b089e65deacbb07ccba)

[Pythonistaなら知らないと恥ずかしい計算量のはなし](https://qiita.com/Hironsan/items/68161ee16b1c9d7b25fb)

[pythonの高速化のために、用途別にcollection型(list/tuple/dictionary/set)の計算量をまとめる](https://qiita.com/bee2/items/4ab87d05cc03d53e19f9)


# 別解
とはいえ、dequeを使っても、PyPyだと間に合ってしまう。おそらくそもそもdequeが結構速い？ちなみに、rotationを愚直に行ったlistでの実装では間に合わなかった。
PyPy: 1423 ms, 106548 KB
Python: TLE
