$(document).ready(function(){

    $('#add').click(function(){

        $('#customers').append('<tr id="row" contenteditable="true"> <td><br></td><td><br></td><td><br></td></tr>');
        
    });

});

window.onload = function () {
    document.getElementById("download")
        .addEventListener("click", () => {
            const invoice = this.document.getElementById("invoice");
            console.log(invoice);
            console.log(window);
            var opt = {
                margin: 1,
                filename: 'TOOLS.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'in', format: 'letter', orientation: 'landscape' }
            };
            html2pdf().from(invoice).set(opt).save();
        })
}
