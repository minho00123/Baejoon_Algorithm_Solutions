function solution(id_pw, db) {
    const id = id_pw[0];
    const pw = id_pw[1];
    
    for (let i = 0; i < db.length; i++) {
        let dbId = db[i][0];
        let dbpw = db[i][1];
        if (dbId === id) {
            if (dbpw === pw) {
                return "login";
            } else {
                return "wrong pw";
            }
            
        }
    }
    return "fail";
}