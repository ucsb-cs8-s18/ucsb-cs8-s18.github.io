    $( document ).ready(function() {

    qd= {
    "version" : "0.1",

  "questions": [ 
   {
    "question": "fr-change-of-base",
      "repeat": 1,
        "parameters": {
          "conversions": [
            { "range": { "min": 0x1000, "max": 0xFFFF }, "radix": { "from": 2, "to": 16 } } 
	  ]
	}
   },
   {
    "question": "fr-change-of-base",
      "repeat": 1,
        "parameters": {
          "conversions": [
            { "range": { "min": 0x1000, "max": 0xFFFF }, "radix": { "from": 16, "to": 2 } } 
	  ]
	}
   },
   {
    "question": "fr-change-of-base",
      "repeat": 1,
        "parameters": {
          "conversions": [
            { "range": { "min": 0x100, "max": 0x1FF }, "radix": { "from": 8, "to": 2 } } 
	  ]
	}
   },
      {
    "question": "fr-change-of-base",
      "repeat": 1,
        "parameters": {
          "conversions": [
            { "range": { "min": 0x100, "max": 0x1FF }, "radix": { "from": 2, "to": 8 } } 
	  ]
	}
   },
      {
    "question": "fr-change-of-base",
      "repeat": 1,
        "parameters": {
          "conversions": [
            { "range": { "min": 0x11, "max": 0x1FF }, "radix": { "from": 10, "to": 2 } } 
	  ]
	}
   },
      {
    "question": "fr-change-of-base",
      "repeat": 1,
        "parameters": {
          "conversions": [
            { "range": { "min": 0x11, "max": 0xFF }, "radix": { "from": 2, "to": 10 } } 
	  ]
	}
   },

      {
    "question": "fr-change-of-base",
      "repeat": 4,
        "parameters": {
          "conversions": [
            { "range": { "min": 0x11, "max": 0xFF }, "radix": { "from": 2, "to": 10 } },
            { "range": { "min": 0x11, "max": 0xFF }, "radix": { "from":10, "to": 2 } },
            { "range": { "min": 0x100, "max": 0x1FF }, "radix": { "from": 2, "to": 8 } },
            { "range": { "min": 0x100, "max": 0x1FF }, "radix": { "from": 8, "to": 2 } },
            { "range": { "min": 0x1000, "max": 0xFFFF }, "radix": { "from": 16, "to": 2 } },
            { "range": { "min": 0x1000, "max": 0xFFFF }, "radix": { "from": 2, "to": 16 } }		
	  ]
	}
   }


   ] }

   
    console.log("ready function called");
    var result= pa.generate("html",JSON.stringify(qd),"abcd1235");
    console.log(result);
    $("#numberConversions").append("<ol>" + result + "</ol>"); 
   });

