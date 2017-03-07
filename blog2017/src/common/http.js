/* eslint-disable */
let $=require('jquery');
let API='http://yulstudio.cn:8082/';
class user {
	constructor() {
  }
	login (data,successFunc,failFunc) {
		$.ajax({
        type: "POST",
        url: API+'auth',
        // The key needs to match your method's input parameter (case-sensitive).
        data: JSON.stringify(data),
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Content-Type", "application/json")
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	create (data,successFunc,failFunc) {
		$.ajax({
        type: "POST",
        url: API+"user/regist",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          //xhr.setRequestHeader ("Content-Type", "application/json")
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	delete(data,token,successFunc,failFunc){
		$.ajax({
        type: "GET",
        url: API+"user/delete",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
					xhr.setRequestHeader ("Authorization", "JWT "+token);
				},
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	revise (data,token,successFunc,failFunc) {
		$.ajax({
        type: "POST",
        url: API+"user/revise",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "JWT "+token);
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	getInfo (data,successFunc,failFunc) {
		$.ajax({
        type: "GET",
        url: API+"user/info",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          //xhr.setRequestHeader ("Content-Type", "application/json")
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	getAll (data,token,successFunc,failFunc) {
		$.ajax({
        type: "GET",
        url: API+"user/all",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "JWT "+token);
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
}
class article{
	constructor() {
  }
	create (data,token,successFunc,failFunc) {
		$.ajax({
        type: "POST",
        url: API+"article/create",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "JWT "+token);
				},
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	revise (data,token,successFunc,failFunc) {
		$.ajax({
        type: "POST",
        url: API+"article/revise",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
					xhr.setRequestHeader ("Authorization", "JWT "+token);
				},
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	getAll (data,successFunc,failFunc) {
		$.ajax({
        type: "GET",
        url: API+"articles",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          //xhr.setRequestHeader ("Content-Type", "application/json")
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	getOne (data,successFunc,failFunc) {
		$.ajax({
        type: "GET",
        url: API+"article",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Content-Type", "application/json")
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	delete (data,token,successFunc,failFunc) {
		$.ajax({
        type: "POST",
        url: API+"article/delete",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
					xhr.setRequestHeader ("Authorization", "JWT "+token);
				},
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	count (data,successFunc,failFunc) {
		$.ajax({
        type: "GET",
        url: API+"article/count",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Content-Type", "application/json")
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	getAlls (data,token,successFunc,failFunc) {
		$.ajax({
        type: "GET",
        url: API+"articles/all",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "JWT "+token);
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
}
class comment{
	constructor() {
  }
	create (data,token,successFunc,failFunc) {
		$.ajax({
        type: "POST",
        url: API+"comment/create",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
					xhr.setRequestHeader ("Authorization", "JWT "+token);
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	getByarticle(data,successFunc,failFunc){
		$.ajax({
        type: "GET",
        url: API+"comment/article",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Content-Type", "application/json")
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	getByson(data,successFunc,failFunc){
		$.ajax({
        type: "GET",
        url: API+"comment/son",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Content-Type", "application/json")
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	count(data,successFunc,failFunc){
		$.ajax({
        type: "GET",
        url: API+"comment/count",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Content-Type", "application/json")
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	delete(data,token,successFunc,failFunc){
		$.ajax({
        type: "GET",
        url: API+"comment/delete",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
					xhr.setRequestHeader ("Authorization", "JWT "+token);
				},
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
	getAll (data,token,successFunc,failFunc) {
		$.ajax({
        type: "GET",
        url: API+"comment/all",
        // The key needs to match your method's input parameter (case-sensitive).
        data: data,
        async: true,
        dataType: "json",
        beforeSend: function (xhr) {
          xhr.setRequestHeader ("Authorization", "JWT "+token);
        },
        success: function(data,status){
					successFunc(data,status);
        },
        error: function(errMsg) {
					failFunc(errMsg);
        }
    });
	}
}
class album {
	constructor(){

	}
	postImg(file,callback){
		let xhr = null;
		let fd=new FormData();
		if (window.XMLHttpRequest){
    	xhr = new XMLHttpRequest();   // 新浏览器
  	}else if (window.ActiveXObject){
			xhr = new ActiveXObject("Microsoft.XMLHTTP");
		}// IE5,IE6
		xhr.open("POST",API+'album/upload', true);
		xhr.onreadystatechange = function() {
			if (xhr.readyState == 4 && xhr.status == 200) {
				// Handle response.
				callback(xhr.responseText); // handle response.
			}
		};
		fd.append('img', file);
		// Initiate a multipart/form-data upload
		xhr.send(fd);
	}
}
let User=new user();
let Article=new article();
let Comment=new comment();
let Album=new album();
export {User, Article, Comment,Album};
