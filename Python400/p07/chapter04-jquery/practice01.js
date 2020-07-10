

$(function () {
    // 全部选择，取消全部选择
    $("#checkAllTop, #checkAllBottom").click(function () {
        var flag = $(this).prop("checked");
        $("input[type=checkbox]").prop("checked", flag);
    });

    // 检查是否全选
    $("input[name=sel]").click(function () {
        var flag = true;
        var sels = $("input[name=sel]");
        sels.each(function () {
            if (!$(this).prop("checked")) {
                flag = false;
            }
        });
        $("#checkAllTop, #checkAllBottom").prop("checked", flag);
    });

    // 增加数量并计算
    $("button[name=add]").click(function () {
        // console.info("clicked");
        var q_input = $(this).prev();
        // console.info(value);
        $(this).prev().attr("value", Number(q_input.val())+1);
        sum(q_input);
    });

    // 减少数量并计算
    $("button[name=sub]").click(function () {
        var q_input = $(this).next();
        if (q_input.val() > 0){
            $(this).next().attr("value", Number(q_input.val())-1);
            sum(q_input);
        }
    });

    // 购物车汇总
    $("input[type=checkbox], button").click(count);

    // 删除单个商品
    $(".del").click(function () {
        $(this).parent().parent().parent().remove();
        count();
    });

    //删除选中商品
    $("#delChecked").click(function () {
        var items = $(".item");
        items.each(function () {
            var flog = $(this).children("ul").children().first().children().prop("checked");
            if (flog) {
                $(this).remove();
            }
        });
        count();
    });
})

// 小计求和
function sum(ele) {
    var q = ele.val();
    var price = ele.parent().prev().html().slice(1);
    ele.parent().next().html("￥" + Number(price) * Number(q));
}

// 商品汇总
function count() {
    console.info("called");
    var items = $(".item");
    console.info("items:" + items)
    var q_count = 0;
    var p_count = 0;
    items.each(function () {
        var ul = $(this).children().first();
        console.info("ul:" + ul);
        var flag = ul.children().first().children().prop("checked");
        console.info(flag);
        if (flag) {
            q_count += Number(ul.children(".p_quantity").children("input").val());
            p_count += Number(ul.children(".p_sum").html().slice(1));
        }
    });
    $("#count_q").html(q_count);
    $("#count_price").html("￥" + p_count);
}
