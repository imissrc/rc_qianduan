 $(document).ready(function() {
    $("#form").validate({
        rules: {
          name: {
            required: true,
            minlength: 2
          },
          telnum: {
            required: true,
            minlength: 5
          },
          mailnum: {
            required: false,
            email: true
          },
        },
        messages: {
          name: {
            required: "请输入用户名",
            minlength: "用户名必需由至少两个字母组成"
          },
          telnum: {
            required: "请输入电话",
            minlength: "电话长度不能小于 5 个字母"
          },
          mailnum: {
            required: "请输入一个正确的邮箱"
          },
        },
        showErrors : function(errorMap, errorList) {
            var msg = "";
            $.each(errorList, function(i, v) {
                msg += (v.message + "\r\n");
            });
            if (msg != "")
                alert(msg);
            },
            onfocusout : false
    });

});