# DrChrono-Challenge by HackerRank
My codes for Dr Chrono Challenge
<!DOCTYPE html>
<html lang="en">
<body>
    <h1>Rock Collectors Jamie and Ned are rock collectors.</h1>
    <p>They store their rocks in a box with partitions where each partition contains a specific type of rock. <br>
    The partitions are numbered from 0 to n 1 where each partition i contains quantity, the number of rocks.<br>
    Both, Jamie and Ned have the box with same partitions.<br>
     Jamie's box is arranged in a random order whereas Ned's box is arranged in a sorted order.<br>
     Geoffrey joins them and observes that the number of rocks in the th partition of his box is the sum of number of rocks in Jamie's ith partition and number of rocks in Ned's ith partition. Find the most frequently curring quantity in Geoffrey's box and return the highest index of the partition with that quantity.<br>
        Note: <ul>
    <li><b> The partitions are 0 indexed.</b></li>
    <li><b> If two or more quantities have the same frequency, then consider the highest quantity among them</b></li>
    </ul>
  Complete the <i><b>get rock_index </i></b>function in the editor below. It has one parameter an array.quantity. of n positive integers.<br>
       It must return an integer denoting the highest index of the partition containing the most frequently occurring quantity in Geoffrey's box.
<br><br>
    <h4>Input Format</h4>
    Locked stub code in the editor reads the following input from stdin and passes it to the function: 
    The first line contains an integer, n, denoting the number of types of rocks.<br>
    Each line i of the n subsequent lines contains integers denoting the number of each type of rock in Jamie's box.<br><br>
    <h4>Constraints<h4>
    <ul>
        <li><i>1 <= n <= 10<sup>5</sup></i></li>
        <li><i> 1 <= quantity<sub>i</sub> <= 10<sup>6</sup></i></li>
    </ul>
    <h4>Output Format</h4>
    Return an integer denoting the highest index of the partition containing the most frequently occurring quantity in Geoffrey's box.
    <h4>Sample Output 0</h4>
    <div style="font-size:12px; background-color:yellow; border:2px solid black; height:100%; width:60%;">
        <p>
        6<br>
        5<br>
        5<br>
            9<br>
            19<br>
            2<br>
         2<br>
        </p>
    </div>
<h4>Sample Output 0</h4>
  <div style="font-size:12px; background-color:gray; border:2px solid black; height:100%; width:60%;">     
         1
   </div>
    </p>
</body>
</html>
