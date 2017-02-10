/* eslint-disable */
function SQLDT() {
    var da = new Date();
    return da.getFullYear() + "-" + (da.getMonth() + 1) + "-" + da.getDate() + " " + da.getHours() + ":" + da.getMinutes() + ":" + da.getSeconds();
}
export default SQLDT;
