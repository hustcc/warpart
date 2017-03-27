function share_weixin(url) {
	document.getElementById("share_weixin_box").innerHTML = '<div class="full_screen_bg" onclick="this.parentNode.innerHTML=\' \';"></div><div class="share_weixin"><a href="javascript:;" onclick="this.parentNode.parentNode.innerHTML=\' \';" class="popup_close">×</a><p>分享到微信朋友圈</p><img class="qrcode" width="200" height="200" src="http://api.setin.cn/qrcode.png?data=' + url + '" /><p>打开微信，点击 + 号菜单的扫一扫，对准二维码扫描即可分享至朋友圈。</p></div>';
	return false;
}
function share_output(url, title, summary) {
	document.write('<div class="share right clearfix"><a href="http://sns.qzone.qq.com/cgi-bin/qzshare/cgi_qzshare_onekey?url=' + url + '&summary=' + summary + '&pics=' + 'http://www.setin.cn/res/atool-org-weixin.jpg' + '?text2img=1&title=' + title + '&site=每日经典美文" class="qzone" title="分享到QQ空间" target="_blank"></a><a href="http://service.weibo.com/share/share.php?title='+ title + '：' + summary + '&url=' + url + '&pic=http://www.atool.org/res/atool-org-weixin.jpg?text2img=1" class="weibo" title="分享到微博" target="_blank"></a><a href="javascript:;" onclick="share_weixin(\'' + url + '#weixin\');return false;" class="weixin" title="分享到微信" target="_blank"></a></div>');
}