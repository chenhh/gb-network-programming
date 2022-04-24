# 泛型(Generics)

## 函數

### 無限制的泛型

```typescript
// 泛型變數
function identity<T>(arg: T): T {
  return arg;
}

// 泛型陣列
function loggingIdentity<T>(arg: T[]): T[] {
  console.log(arg.length);
  return arg;
}

// 泛型函數指標
let myIdentity: <T>(arg: T) => T = identity;
```
