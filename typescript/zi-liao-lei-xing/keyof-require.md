# keyof, require,

## 簡介

keyof 與 Object.keys 略有相似，只不過 keyof 取 interface 的鍵。

```typescript
interface Point {
  x: number;
  y: number;
}

// 相當於:
// type keys = "x" | "y"
type keys = keyof Point;
```

#### 應用

假設有一個 object 如下所示，我們需要使用 typescript 實現一個 get 函數來獲取它的屬性值：

```javascript
const data = {
  a: 3,
  hello: 'world'
}

function get(o: object, name: string) {
  return o[name]
}
```

我們剛開始可能會這麼寫，不過它有很多缺點

* 無法確認返回類型：這將損失 ts 最大的類型校驗功能。
* 無法對 key 做約束：可能會犯拼寫錯誤的問題。

解法：這時可以使用 keyof 來加強 get 函數的類型功能。

```typescript
function get<T extends object, K extends keyof T>(o: T, name: K): T[K] {
  return o[name]
}
```

## key any

```typescript
// 以下兩者等效，但適用 keyof 更加簡短
type PropertyName = keyof any;
type PropertyName = string | number | symbol;
```

## Pick、Require, Partial

既然瞭解了 keyof，可以使用它對屬性做一些擴展， 如實現 Partial 和 Pick，Pick 一般用在 \_.pick 中。

```typescript
// 只要有部份T的屬性即可
type Partial<T> = {
  [P in keyof T]?: T[P];
};
// 必須要有T的全部屬性
type Required<T> = {
  [P in keyof T]-?: T[P];
};

// 滿足從T中自訂部份屬性即可
type Pick<T, K extends keyof T> = {
  [P in K]: T[P];
};

interface User {
  id: number;
  age: number;
  name: string;
};

// 相當於: type PartialUser = { id?: number; age?: number; name?: string; }
type PartialUser = Partial<User>

// 相當於: type PickUser = { id: number; age: number; }
type PickUser = Pick<User, 'id' | 'age'>t
```

## Condition Type

類似於 js 中的 ?: 運算符，可以使用它擴展一些基本類型。

```typescript
type isTrue<T> = T extends true ? true : false

// 相當於 type t = false
type t = isTrue<number>

// 相當於 type t = false
type t = isTrue<false>
```

## never & Exclude & Extract & Omit

never 的描述如下：the never type represents the type of values that never occur。

結合 never 與 conditional type 可以推出很多有意思而且實用的類型，比如 Exclude 與 Extract。

```typescript
type Exclude<T, U> = T extends U ? never : T;

// 相當於: type A = 'a'
type A = Exclude<'x' | 'a', 'x'>
type A = Exclude<'x' | 'a', 'x' | 'y' | 'z'>

// 與 Exclude 實現剛好相反，Exclude 取差集，而 Extract 取交集
type Extract<T, U> = T extends U ? T : never;

// 相當於: type A = 'x'
type A = Exclude<'x' | 'a', 'x'>
```

```typescript
type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;

interface User {
  id: number;
  age: number;
  name: string;
};

// 相當於: type PickUser = { age: number; name: string; }
type OmitUser = Omit<User, "id">
```

## typeof

顧名思義，typeof 代表取某個值的 type。

```typescript
const a: number = 3

// 相當於: const b: number = 4
const b: typeof a = 4
```

在一個典型的服務端項目中，我們經常需要把一些工具塞到 context 中，如config，logger，db models, utils 等，此時就使用到 typeof。

```typescript
import logger from './logger'
import utils from './utils'

interface Context extends KoaContect {
  logger: typeof logger,
  utils: typeof utils
}

app.use((ctx: Context) => {
  ctx.logger.info('hello, world')

  // 會報錯，因為 logger.ts 中沒有暴露此方法，可以最大限度的避免拼寫錯誤
  ctx.loger.info('hello, world')
})
```

## is

可以使用 is 來判定值的類型。

```typescript
function isAxiosError (error: any): error is AxiosError {
  return error.isAxiosError
}

if (isAxiosError(err)) {
  code = `Axios-${err.code}`
}
```

## interface & type

一般來說，interface 與 type 區別很小，比如以下兩種寫法差不多.&#x20;

```typescript
interface A {
  a: number;
  b: number;
};

type B = {
  a: number;
  b: number;
}
```

其中 interface 可以如下合並多個，而 type 只能使用 & 類進行連接。

```typescript
interface A {
    a: number;
}

interface A {
    b: number;
}

const a: A = {
    a: 3,
    b: 4
}
```

## 使用 const enum 維護常量表

相比使用字面量對象維護常量，const enum 可以提供更安全的類型檢查。

```typescript
// 使用 object 維護常量
const TODO_STATUS {
  TODO: 'TODO',
  DONE: 'DONE',
  DOING: 'DOING'
}

// 使用 const enum 維護常量
const enum TODO_STATUS {
  TODO = 'TODO',
  DONE = 'DONE',
  DOING = 'DOING'
}

function todos (status: TODO_STATUS): Todo[];

todos(TODO_STATUS.TODO)
```
