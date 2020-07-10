
$(function () {
    // 全选或取消全选
    $("#chks").click(function () {
        var flag = $(this).prop("checked");
        $("input[name='chk']").prop("checked", flag);
    })

    // 检查全选
    $("input[name=chk]").click(function () {
        var flag = true;
        $("input[name=chk]").each(function () {
            if (!$(this).prop("checked")) {
                flag = false;
            }
        });
        $("#chks").prop("checked", flag);
    })

    // 反选
    $("#fx").click(function () {
        var chks = $("input[type=checkbox]");
        chks.each(function () {
            var flag = $(this).prop("checked");
            $(this).prop("checked", !flag);
        });
    });

    // 新增一行
    $("#addRow").click(function () {
            var table = $("#ta");
            table.append($('\t\t\t<tr id="">\n' +
                '\t\t\t\t<td><input type="checkbox" name="chk" id="" value="2"/></td>\n' +
                '\t\t\t\t<td>《Java编程之道》</td>\n' +
                '\t\t\t\t<td>wollo</td>\n' +
                '\t\t\t\t<td>10</td>\n' +
                '\t\t\t\t<td>\n' +
                '\t\t\t\t\t<input type="button" name="aa" id="" value="修改数量"  />\n' +
                '\t\t\t\t\t<input type="button" name="" id="" value="删除" />\n' +
                '\t\t\t\t</td>\n' +
                '\t\t\t</tr>'));
    });

    // 删除选中的行
    $("#delRow").click(function () {
        var trs = $("input[name=chk]:checked");
        if (trs.length === 0 ) {
            alert("请选择要删除的书籍");
        } else {
            trs.parent().parent().remove();
        }
    });

    // 复制选中行
    $("#copyRow").click(function () {
        var trs = $("input[name=chk]:checked");
        if (trs.length === 0 ) {
            alert("请选择要复制的书籍");
        } else {
            $("#ta").append($(trs.parent().parent().clone()));
        }
    });

    // 修改数量
    // 已知问题：无法动态绑定
    $("input[name=changeQ]").click(function () {
        var ele = $(this).parent().parent().children().eq(3);
        ele.html("<input type='text' size='3px' onblur='saveValue(this)'/>");
    });

    // 删除节点
    // 已知问题：无法动态绑定
    $("input[name=delete]").click(function () {
        var ele = $(this).parent().parent();
        ele.remove();
    });
})

// 应用更改
function saveValue(ele) {
    $(ele).parent().html(ele.value);
}