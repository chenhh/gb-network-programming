# asyncio

## 簡介



asyncio是用在IO密集型和高層級結構化網路程式碼(因為網路傳輸和IO一樣需要等待很多時間)的最佳選擇。

asyncio 觀念很簡單，會有一個 thread 去跑所有的 work，在此叫他 event loop(在此用 work 而不用 task 的原因是，task 是 asynio 裡的一個類別，為了避免混淆，所以用 work)。&#x20;

work 是透過呼叫 "async def" 的 function 所建立的，event loop 一次只會執行一個 work。當 event loop 執行 work 時，遇到 await 時，就會讓其他 work 先執行。等到他 await 的東西好了，該 work 會重新進入排程，等待被 event loop 執行。&#x20;

非同步程式設計的上下文中，事件無比重要。因為事件的本質就是非同步。

## 阻塞和非阻塞 (Blocking & Non-blocking)

阻塞這概念是指一個函數執行後，會不會一直等回傳結果才做下一件事情，阻塞和非阻塞關注的是程式在等待呼叫結果（訊息，返回值）時的狀態。

例如去買書，問老闆有沒有書，阻塞程序就會等回傳後的結果後才會進行下一步，非阻塞則是在問有沒有書的同時就去旁邊玩沙了，過一會兒再來看看有沒有回傳結果。
