<?php
	require_once ('twitteroauth.php');
	require_once( 'cron.class.php' );
	/**********************************************************************************************/
	$pdo = new CronDB();
	$pdo->query("SELECT count(*) as counter FROM table WHERE counter = 0");
	$row = $pdo->row();
	if(isset($row['counter'] && $row['counter'] > 1) {
		DoAnagram();
	} else {
		$pdo->query("UPDATE table SET counter='0' WHERE ID > 0 ");
		$pdo->execute();
		DoAnagram();
	}
	
	function DoAnagram() {
		$pdo->query("SELECT ID, field FROM table WHERE counter = 0 ORDER BY RAND() LIMIT 1");
		$row = $pdo->row();
		$name = str_replace('_','',$row['field']);
			$anagram  = str_shuffle($name);
			$answer = $pdo->_V($row['field']);
		$id = $row['ID'];
		$pdo->Tweet("anagram : {$anagram}");
		$pdo->query("UPDATE table SET counter='1' WHERE ID = :id ");
		$pdo->bind(':id',$id);
		$pdo->execute();
		sleep(1200);
		$pdo->Tweet("answer was : {$answer}");
	}
