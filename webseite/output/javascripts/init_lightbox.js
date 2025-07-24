$(function() {
	if($("#galerie a")) 
		$("#galerie a").lightBox({fixedNavigation:true});
		
	if($("#fotogalerie a"))
		$("#fotogalerie a").lightBox({fixedNavigation:false, txtImage:"Foto"});
});