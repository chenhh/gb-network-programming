# 迴圈與迭代

## for

```javascript
for(let idx=0; idx<10; ++idx){
    console.log(idx);
}
// 0
// ...
// 9
```

## for in

for...in 陳述式重複一個指定的變數來迴圈<mark style="color:red;">一個物件所有可列舉的屬性</mark>。

```javascript
// 迴圈這個物件的所有屬性並傳回一個列出屬性名和值的字串。
function dump_props(obj, obj_name) {
  let result = "";
  for (var i in obj) {
    result += obj_name + "." + i + " = " + obj[i] + "<br>";
  }
  result += "<hr>";
  return result;
}
```

雖然用for...in來迭代 Array 元素很吸引人，但是它傳回的除了數字的索引之外還有可能是你自己定的屬性名。

## for of

for...of 陳述式在iterable objects(可迭代的物件)上建立了一個迴圈 (包含 Array, Map, Set, arguments(引數) 物件 等等), 對每個獨特屬性的值使用一個準備被執行的有陳述式的自訂迭代掛勾。

<mark style="color:red;">for...in 在屬性名字迴圈，而for...of 在屬性的值迴圈</mark>。

```javascript
let arr = [3, 5, 7];
arr.foo = "hello";

for (let i in arr) {
   console.log(i); // "0", "1", "2", "foo"
}

for (let i of arr) {
   console.log(i); // 3, 5, 7
}
```

## do while

```javascript
let i = 0;
do {
    i += 1;
    console.log(i);
} while (i < 5);
// 1
// ...
// 5
```

## while

```javascript
let n = 0;
let x = 0;
while (n < 3) {
  n++;
  x += n;
}
// 6
```

## label&#x20;

label 提供一個有識別字的陳述式讓你能在程式的別的地方參考。舉個例子，你能使用label 來識別一個迴圈，然後使用break或continue陳述式來指示何時程式該中斷迴圈或是繼續他的執行。

```javascript
// markLoop這個label 識別一個while 迴圈
markLoop:
while (theMark == true) {
   doSomething();
}
```

## break

break 陳述式是用來終止一個迴圈，一個switch多重控制選項，或是和一個label陳述式聯合使用。

```javascript
// break for loop
for (let i = 0; i < a.length; i++) {
  if (a[i] == theValue) {
    break;
  }
}
```

```javascript
// break a label
let x = 0;
let z = 0;
labelCancelLoops: while (true) {
  console.log("Outer loops: " + x);
  x += 1;
  z = 1;
  while (true) {
    console.log("Inner loops: " + z);
    z += 1;
    if (z === 10 && x === 10) {
      break labelCancelLoops;
    } else if (z === 10) {
      break;
    }
  }
}
```

## continue

continue 陳述式可以用於重新開始一個 while , do-while, for, 或 label 陳述式。

```javascript
// continue while
let i = 0;
let n = 0;
while (i < 5) {
  i++;
  if (i == 3) {
    continue;
  }
  n += i;
}
```

```javascript
// continue a label
checkiandj:
  while (i < 4) {
    console.log(i);
    i += 1;
    checkj:
      while (j > 4) {
        console.log(j);
        j -= 1;
        if ((j % 2) == 0) {
          continue checkj;
        }
        console.log(j + " is odd.");
      }
      console.log("i = " + i);
      console.log("j = " + j);
  }
```
