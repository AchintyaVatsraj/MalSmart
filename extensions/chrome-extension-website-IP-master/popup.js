var chrome = window.chrome;

function updateButtonStatus() {
	chrome.extension.sendMessage({name: 'isEnabled'}, function(isEnabled) {
		// summary:
		//		set the button to the correct value

		//reverse because the value represent the opposite of current
		document.querySelector('#enableDisableIPButton').value = isEnabled ? 'false' : 'true';
		document.querySelector('#enableDisableIPButton').innerHTML = chrome.i18n.getMessage(isEnabled ? 'disable' : 'enable');
	});
}

document.querySelector('#enableDisableIPButton').addEventListener('click', function() {
	// summary:
	//		Attach the click event

	if(document.querySelector('#enableDisableIPButton').value === 'false') {
		chrome.extension.sendMessage({name: 'setEnabled', status: false}, updateButtonStatus);
	} else {
		chrome.extension.sendMessage({name: 'setEnabled', status: true}, updateButtonStatus);
	}
});

document.querySelector('#copyToClipboard').addEventListener('click', function() {
	// content script
	chrome.extension.sendMessage({
		name: 'copyIP'
	});
});

updateButtonStatus();