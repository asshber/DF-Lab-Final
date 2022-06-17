rule malicious{
	strings:
		$error_msg0="gethostbyname"
		$error_msg1="setsockopt"
		$error_msg2="Usage:"
		$error_msg3="connect"
		$unique_str="GET /Me5HIC2ibF"
	condition:
		$error_msg0 and $error_msg1 and $error_msg2 and $error_msg3 and $unique_str
	}
