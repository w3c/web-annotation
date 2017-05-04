// @license: W3C Software and Document Notice and License, https://www.w3.org/Consortium/Legal/2015/copyright-software-and-document
// @author: Ivan Herman


$(document).ready(function() {
	/* -------------
	   URI -> Selector. Note that the real meat is in the parser, to be
	   included in HTML separately
	---------------*/
	$("#u-to-s").click( function() {
		// Parse a fragment and display the result...
		var the_uri  = $("#uri").val().trim();
		var uri = undefined;
		var fragment = "";
		var splitted = the_uri.split('#');


		if( splitted.length == 2 ) {
			uri      = splitted[0];
			fragment = splitted[1]
		} else {
			fragment = the_uri
		}
		try {
			var selector = Parser.parse(fragment);
			selector.source = uri;
			$("#selector").val(JSON.stringify(selector, null, '    '))
		} catch( err ) {
			$("#selector").val("***** " + err.message + " *****");
		}
	});

	/* -------------
	   Selector -> URI.
	---------------*/

	function convert_to_url( obj ) {

		function state_or_selector(obj) {
			// Deciding whether the object is a selector or a state...
			return (obj.type === "TimeState" || obj.type === "HttpRequestState") ? "state" : "selector";
		}

		function encode_value( val ) {
			return encodeURI(val)
				.replace(/#/g,'%23')
				.replace(/,/g,'%2C')
				.replace(/=/g,'%3D')
				.replace(/%5B/gi,'[')
				.replace(/%5D/gi,']')
				.replace(/%3E/gi,'>')
				.replace(/%3C/gi,'<')
		}

		function frag(fname, obj) {
			function key_val(val, key) {
				// Create either a key=val string or, for some specific key values
				// calls recursively the fragment generator with that key.
				// The only mini-complication is that the 'function' name for the recursion should
				// be derived from the object (which is either a state for refinement, or a range selector)
				// The unusual order of the arguments is because the function is to be used in _.map, which imposes
				// this order
				if( key === 'refinedBy' || key === "startSelector" || key === "endSelector" ) {
					return key + '=' + frag(state_or_selector(val), val);
				} else {
					return key + '=' + encode_value(val)
				}
			}

			if( typeof(obj) === 'string' ) {
				// in practice: this is a uri
				return fname + '=' + encode_value(obj)
			} else {
				return fname + "(" + _.map(obj, key_val) + ")"
			}
		}

		uri = obj.source;
		if( obj.selector !== undefined ) {
			fragment = frag("selector", obj.selector);
		} else if (obj.state !== undefined ) {
			fragment = frag("state", obj.state)
		}

		return (uri !== undefined) ? uri + '#' + fragment : fragment

	}

	$("#s-to-u").click(function() {
		try {
			var selector = JSON.parse($("#selector").val());
			$("#uri").val( convert_to_url(selector) );
		} catch(err) {
			$("#uri").val("***** " + err.message + " *****");
		}
	})
});
