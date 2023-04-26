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
    getjournal: baseURL + "/journalinformation/list/get",
    createjournal: baseURL + "/journalinformation/list/create",
    getjournalscore: baseURL + "/journalinformation/score/get",
    getjournalnamelist: baseURL + "/journalinformation/list/getjournalnamelist"
}

export const citationURL = {
    getDocCount: baseURL + "/journalcitation/doc_count",
    getCiteCount: baseURL + "/journalcitation/cited_count",
    getIF: baseURL + "/journalcitation/IF",
    getAvgCiteCount: baseURL + "/journalcitation/avg_cite_count",
    getTwoYearsCitation: baseURL + "/journalcitation/two_years_citation",
    getAll: baseURL + "/journalcitation/get",
}