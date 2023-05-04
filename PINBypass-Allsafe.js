Java.perform(function(){
	Java.choose('infosecadventures.allsafe.challenges.PinBypass',{
		onMatch: function(instance){
			for(var i=1000;i<10000;i++)
			{
				console.log("Checking "+i.toString())
				if(instance.checkPin(i.toString())== true)
				{
					console.log("Pin found : "+i.toString());
					break;
				}
			}
	},
	onComplete: function() {}
	});
});
