<!DOCTYPE html>
<html>
<head>
    <title>Flag Submit</title>
</head>
<body>
    <?php
        include("item.php");

        for($i = 0; $i < 6; $i++) {
            $form = '
        <form method="post" action="check.php">
        <div style="margin-left:10%;">
                <h1>'.$title[$i].'</h1>
                <a href="'.$file_list[$i].'">Challenge Download</a><br>
                <b>'.$link_list[$i].'</b><br>
                <input type="text" value="" name="nickname" placeholder="nickname">
                <input type="text" value="" name="flag" placeholder="flag">
                <input type="hidden" value="'.$name[$i].'" name="challenge">
                <input type="submit">
        </div>
        </form>
        ';
                echo $form;
        }
?>
        <img src='cheers.gif' alt="" style="float:right;margin-top:-30%;margin-right:10%;width:50%;height:100%;border-radius:30px;"/>
</body>
</html>
