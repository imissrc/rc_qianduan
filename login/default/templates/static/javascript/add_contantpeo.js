 $(document).ready(function() {
   $("form :input.req").each(function() {
        //通过jquery api：$("HTML字符串") 创建jquery对象
        var $required = $("<strong class='high'>*</strong>");
        //添加到this对象的父级对象下
        $(this).parent().append($required);
    });
    $("form :input").blur(function() {
        var $parent = $(this).parent();
        $parent.find(".msg").remove();
        //验证姓名
        if ($(this).is("#username")) {
            var nameVal = $.trim(this.value); //原生js去空格方式：this.replace(/(^\s*)|(\s*$)/g, "")
            var regName = /[~#^$@%&!*()<>:;'"{}【】  ]/;
            if (nameVal == "" || nameVal.length < 6|| regName.test(nameVal)) {
                var errorMsg = "*";
                //class='msg onError' 中间的空格是层叠样式的格式
                $parent.append("<span class='msg onError'>" + errorMsg + "</span>");
            } else {
                var okMsg = "√";
                $parent.find(".high").remove();
                $parent.append("<span class='msg onSuccess'>" + okMsg + "</span>");
            }
        }
        // 验证密码
        if ($(this).is("#telnum")) {
            var telnumVal = $.trim(this.value);
            var regTelnum = /\d{7,11}/;
            if (telnumVal == "" || (telnumVal != "" && !regTelnum.test(telnumVal))) {
                var errorMsg = "*";
                $parent.append("<span class='msg onError'>" + errorMsg + "</span>");
            } else {
                var okMsg = "√";
                $parent.find(".high").remove();
                $parent.append("<span class='msg onSuccess'>" + okMsg + "</span>");
            }
        }
    }).keyup(function() {
        //triggerHandler 防止事件执行完后，浏览器自动为标签获得焦点
        $(this).triggerHandler("blur");
    }).focus(function() {
        $(this).triggerHandler("blur");
    });

    //点击登录按钮时，通过trigger()来触发文本框的失去焦点事件

    $("#btn_save").click(function() {
        //trigger 事件执行完后，浏览器会为submit按钮获得焦点
        $("form .text_field:input").trigger("blur");
        var numError = $("form .onError").length;
        if (numError) {
            return false;
        }

    });
});