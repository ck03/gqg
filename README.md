# gqg
青島政務網政府信箱爬蟲<br/>
爬取問題:
<ul>
<li>1.有的項目要有查詢碼,應該是個人設定不允許別人觀看只限本人,所以就要排除,排除方式找到規則==><a target="_blank" title="心怡苑搭建临时房问题" onclick="ViewReplyCheck('{20190922-2359-1742-2727-FA163E60C32B}','0')" >
  當ViewReplyCheck第二個參數是 0 時,則是有查詢碼跳過不查, 是 1 時才查</li>
<li>2.本例使用selenium的原因,因為雖然可以從爬取的資料中串成內容頁的網址,再去request.get,但是這樣的方式會被網站排除,導到錯誤頁面,所以使用selenium模擬網頁的操作去click才能正確取得內容頁的資料,又會另開視窗,所以這裡使用2個driver對象來操作</li>
  </ul>
