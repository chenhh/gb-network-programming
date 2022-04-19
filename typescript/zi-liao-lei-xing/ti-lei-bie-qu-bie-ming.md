# 替類別取別名

## 簡介

```typescript
export type Nominal<T, Name extends string> = T & {
	/** The 'name' or species of the nominal.
	 * Name為自訂類型名稱(字串), T為基礎類型
	 * & 為intersection types, 將T與{[Symbol.species]: Name;}的屬性聯集
	 * */
	[Symbol.species]: Name;
};
```

可以將基礎名稱取別名如Nomial\<number, "T1">, Nomial\<number, "T2"> 上面兩個類別雖然基礎類別都是number，但是ts將其視為類別T1, T2。

```typescript
type Index = Nominal<number, 'Index'>;
type Index2 = Nominal<number, 'Index2'>;
let i: Index = 42 as Index; 
let j: Index2 = 42 as Index2; 
console.log(typeof i); // number
console.log(typeof j); // number
// i === j; error, always false
console.log(typeof i === typeof j); // true
```
