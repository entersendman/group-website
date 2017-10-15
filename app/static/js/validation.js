function checkMail(email) {
    return /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/.test(email);           
}
function checkPhone(phone) {
    return /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/.test(phone);           
}
function checkLocation(location) {
    return /^([a-z0-9_-]+\.)*[a-z0-9_-]+@[a-z0-9_-]+(\.[a-z0-9_-]+)*\.[a-z]{2,6}$/.test(phone);           
}
function checkName(name) {
    return /(^[A-Z]{1}[a-z]{1,14} [A-Z]{1}[a-z]{1,14}$)/.test(phone);           
}
