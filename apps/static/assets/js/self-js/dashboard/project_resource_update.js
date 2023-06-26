function editProjectResource() {
    $('#edit-Modal').on('show.bs.modal', function (event) {
        var $this = $(this);
        var button = $(event.relatedTarget); // Button that triggered the modal
        var recipient = button.attr('data-bs-whatever');
        var user_rsrc_arr = eval(recipient);
        var id = user_rsrc_arr[0];
        var username = user_rsrc_arr[1];
        var jan = user_rsrc_arr[2];
        var feb = user_rsrc_arr[3];
        var mar = user_rsrc_arr[4];
        var apr = user_rsrc_arr[5];
        var may = user_rsrc_arr[6];
        var jun = user_rsrc_arr[7];
        var jul = user_rsrc_arr[8];
        var aug = user_rsrc_arr[9];
        var sep = user_rsrc_arr[10];
        var oct = user_rsrc_arr[11];
        var nov = user_rsrc_arr[12];
        var dec = user_rsrc_arr[13];
        var modal = $(this);
        modal.find('#modal-title').text('Update Resource-'+username);
        modal.find('#id-display').val(id)
        modal.find('#username-display').val(username)
        modal.find('#inputJan').val(jan)
        modal.find('#inputFeb').val(feb)
        modal.find('#inputMar').val(mar)
        modal.find('#inputApr').val(apr)
        modal.find('#inputMay').val(may)
        modal.find('#inputJun').val(jun)
        modal.find('#inputJul').val(jul)
        modal.find('#inputAug').val(aug)
        modal.find('#inputSep').val(sep)
        modal.find('#inputOct').val(oct)
        modal.find('#inputNov').val(nov)
        modal.find('#inputDec').val(dec)
    })
}

function updateProjectResource() {
    $('.row-update-btn').on('click', function (event) {
        var $this = $(this);
        var modal_body = $this.parents('.modal-footer').siblings('.modal-body');
        var user_id = modal_body.find('#id-display').val();
        var username = modal_body.find('#username-display').val();
        var jan = modal_body.find('#inputJan').val();
        var feb = modal_body.find('#inputFeb').val();
        var mar = modal_body.find('#inputMar').val();
        var apr = modal_body.find('#inputApr').val();
        var may = modal_body.find('#inputMay').val();
        var jun = modal_body.find('#inputJun').val();
        var jul = modal_body.find('#inputJul').val();
        var aug = modal_body.find('#inputAug').val();
        var sep = modal_body.find('#inputSep').val();
        var oct = modal_body.find('#inputOct').val();
        var nov = modal_body.find('#inputNov').val();
        var dec = modal_body.find('#inputDec').val();
        message={};
        message["user_id"]=user_id;
        message["project_id"]=table_datadict['project_id'];
        message["year"]=table_datadict['year'];
        message["username"]=username;
        message["Jan"]=jan;
        message["Feb"]=feb;
        message["Mar"]=mar;
        message["Apr"]=apr;
        message["May"]=may;
        message["Jun"]=jun;
        message["Jul"]=jul;
        message["Aug"]=aug;
        message["Sep"]=sep;
        message["Oct"]=oct;
        message["Nov"]=nov;
        message["Dec"]=dec;
        var data = JSON.stringify(message);
        alert(data)
        $.ajax({
            url: "/update-project-resource",
            method: "POST",
            data: data,
            success: function () {
                alert("更新成功");
                // $this.parents('caption').siblings().find('td.percent-display').css("color","red");
                location.reload(true);
            },
            error: function () {
                alert("更新失败");
            }
        })
    })
}


// 等网页文档所有元素加载完成后再执行
$(function () {
    editProjectResource();
    updateProjectResource();
});