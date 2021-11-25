var chrome = window.chrome;

chrome.extension.sendMessage({name: 'isEnabled'}, function(isEnabled) {
	// summary:
	//		only do stuff if enabled
	if(!isEnabled) { return; }

	chrome.extension.sendMessage({name: 'getIP'}, function(response) {
		// summary:
		//		grab the ip

		if(!response.ip || response.ip === '::') { return; }

		var websiteip = document.createElement('websiteip');

		websiteip.id = 'chrome_websiteIP';
		websiteip.className = 'chrome_websiteIP_right';
		websiteip.innerHTML = response.ip;
		if(document && document.body) {
			document.body.appendChild(websiteip);
		}

		websiteip.addEventListener('mouseover', function() {
			if(this.className.indexOf('chrome_websiteIP_right') !== -1) {
				this.className = this.className.replace('chrome_websiteIP_right', 'chrome_websiteIP_left');
			} else {
				this.className = this.className.replace('chrome_websiteIP_left', 'chrome_websiteIP_right');
			}
		}, false);
	});});