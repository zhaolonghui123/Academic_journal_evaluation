const baseURL = 'http://localhost:8080/api'
export const userURL = {
    getAllUser: baseURL + "/user/get",
    delUser: baseURL + "/user/delete",
    create: baseURL + "/user/create",
}

export const journalURL = {
    getOnePapercount: baseURL + "/journal/get_one",
    getPapercount:baseURL + "/journal/get",
    gettest: baseURL + "/journal/test",
    getjournalInfo: baseURL + "/journalinformation/get",
}