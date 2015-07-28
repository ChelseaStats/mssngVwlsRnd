<?php
	require_once ('twitteroauth.php');
	require_once( 'cron.class.php' );
	/**********************************************************************************************/
	$pdo = new CronDB();
	$pdo->query("SELECT count(*) as counter FROM table WHERE counter = 0");
	$row = $pdo->row();
	if(isset($row['counter'] && $row['counter'] > 1) {
		mssngVwls();
	} else {
		$pdo->query("UPDATE table SET counter='0' WHERE ID > 0 ");
		$pdo->execute();
		mssngVwls();
	}
	
	function mssngVwls() {
		$pdo->query("SELECT ID, field FROM table WHERE counter = 0 ORDER BY RAND() LIMIT 1");
		$row 		= $pdo->row();
		$name 		= str_replace('_','',$row['field']);
		$vowels 	= array("a", "e", "i", "o", "u", "A", "E", "I", "O", "U", " ");
		$name 		= str_replace($vowels, "", $name);
		$length 	= strlen($name);
		$random 	= rand(1,$length);
		$mssngVwls 	= strrev(chunk_split (strrev($mssngVwls), $random,' '));
		$answer 	= $pdo->_V($row['field']);
		$id 		= $row['ID'];
		$pdo->Tweet("Missng vowels game : {$mssngVwls}");
		$pdo->query("UPDATE table SET counter='1' WHERE ID = :id ");
		$pdo->bind(':id',$id);
		$pdo->execute();
		sleep(1200);
		$pdo->Tweet("Answer was : {$answer}. Congratulations if you got it.");
	}
