<h1 align = "center">Script break down</h1>

<h3>First things to know<h3>
   <ul>
     <li>It is done in Python 3</li>
     <li>It is not require to download anything</li>
      <li>Feel free to use it, that would make me happy :hugs:</li>
   </ul>

<h3>Library used</h3>

```
import re
```

<h3>What Credit cards are valid?</h3>
   <ul>
      <li>American Express</li>
      <li>VISA</li>
      <li>Mastercard</li>
   </ul>

<h3>Constants to know to which company belongs the credit card</h3>
   <h4>VISA</h4>
      <p>Conditions</p>
         <ul>
            <li>Start with 4</li>
            <li>Has a lenght of 13 or 16</li>
         </ul>
   <h4>Mastercard</h4>
      <p>Conditions</p>
         <ul>
            <li>Start with 51, 52, 53, 54 or 55</li>
            <li>Has a lenght of 16</li>
         </ul>
<h4>American Express</h4>
      <p>Conditions</p>
         <ul>
            <li>Start with 34 or 37</li>
            <li>Has a lenght of 15</li>
         </ul>   
