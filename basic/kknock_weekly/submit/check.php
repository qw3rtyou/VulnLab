<?php

    include("item.php");
    
    $nickname = $_POST['nickname'];
    $flag = $_POST['flag'];
    $challenge = $_POST['challenge'];

    if(empty($nickname)) {
        echo "<script>alert('Enter the Nickname!');location.href='index.php'</script>";
    }
    else if(empty($flag)) {
        echo "<script>alert('Enter the Flag!');location.href='index.php'</script>";
    }
    else {
        if($challenge == $name[0] && $flag === "KCTF{I_d0nt_lik3_pick13}") {
            $fp = fopen("solved.5un9hun.solved", 'ab+');
            fwrite($fp, iconv('UTF-8','euc-kr//IGNORE', "[".$nickname."] ".$challenge."\t".$flag."\t[solved]\n"));
            echo "<script>alert('Congratz! ".$challenge." Solved.');location.href='index.php'</script>";
        }
        else if($challenge == $name[1] && $flag === "flag{https://dreamhack.io/wargame/challenges/1054}") {
            $fp = fopen("solved.5un9hun.solved", 'ab+');
            fwrite($fp, iconv('UTF-8','euc-kr//IGNORE', "[".$nickname."] ".$challenge."\t".$flag."\t[solved]\n"));
            fclose($fp);
            echo "<script>alert('Congratz! ".$challenge." Solved.');location.href='index.php'</script>";
        }
        else if($challenge == $name[2] && $flag === "hECQh25nU3RhciEbA9WT") {
            $fp = fopen("solved.5un9hun.solved", 'ab+');
            fwrite($fp, iconv('UTF-8','euc-kr//IGNORE', "[".$nickname."] ".$challenge."\t".$flag."\t[solved]\n"));
            fclose($fp);
            echo "<script>alert('Congratz! ".$challenge." Solved.');location.href='index.php'</script>";
        }
        else if($challenge == $name[3] && $flag === "flag{dreamhackezrevbbbbb}") {
            $fp = fopen("solved.5un9hun.solved", 'ab+');
            fwrite($fp, iconv('UTF-8','euc-kr//IGNORE', "[".$nickname."] ".$challenge."\t".$flag."\t[solved]\n"));
            fclose($fp);
            echo "<script>alert('Congratz! ".$challenge." Solved.');location.href='index.php'</script>"; 
        }
        else if($challenge == $name[4] && $flag === "ftz{https://dreamhack.io/wargame/challenges/106}") {
            $fp = fopen("solved.5un9hun.solved", 'ab+');
            fwrite($fp, iconv('UTF-8','euc-kr//IGNORE', "[".$nickname."] ".$challenge."\t".$flag."\t[solved]\n"));
            fclose($fp);
            echo "<script>alert('Congratz! ".$challenge." Solved.');location.href='index.php'</script>";
        }
        else if($challenge == $name[5] && $flag === "ftz{dr34mh4ck_sw1tch1ng_c0mm4nd_h3h3}") {
            $fp = fopen("solved.5un9hun.solved", 'ab+');
            fwrite($fp, iconv('UTF-8','euc-kr//IGNORE', "[".$nickname."] ".$challenge."\t".$flag."\t[solved]\n"));
            fclose($fp);
            echo "<script>alert('Congratz! ".$challenge." Solved.');location.href='index.php'</script>";
        }
        else {
            echo "<script>alert('Oops.. Are you guessing?');location.href='index.php'</script>";
        }
    }  
?>
