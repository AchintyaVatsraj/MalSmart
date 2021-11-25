var chrome = window.chrome,
	nodes = document.getElementsByTagName('*'),
	j,
	node,
	innerHTML,
	newInnerHTML,
	matcher = function(dummyMatch, value) {
		// summary:
		//		proceed the value, if needed
		return value ? chrome.i18n.getMessage(value) : '';
	};

for(j = nodes.length - 1; j > 0; j--) {
	node = nodes[j];

	innerHTML = node.innerHTML.toString();
	newInnerHTML = innerHTML.replace(/__MSG_(\w+)__/g, matcher);

	if(newInnerHTML !== innerHTML) {
		node.innerHTML = newInnerHTML;
	}
}
