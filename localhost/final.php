<?php   
      $joke = $_GET['j'];
      $time = $_GET['t'];
      $time .= "m"
?>
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet/less" href="style.less">
	<script src="less.js"></script>
</head>
<body>
	<div id="content">
		<div class="wrapper">
			<div id="ribbits" class="panel left">
				<div class="ribbitWrapper">
					<img class="avatar" src="gfx/user2.png">
					<span class="name">I_joke</span> @I_joke <span class="time"><?php echo $time; ?></span>
					<p style="font-size:22px;">
						<?php echo $joke; ?>
					</p>
				</div>
			</div>
		</div>
	</div>
</body>
</html>
