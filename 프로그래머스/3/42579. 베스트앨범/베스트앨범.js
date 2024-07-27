function solution(genres, plays) {
    const answer = [];
    const genresObj = {};
    const playObj = {};
    
    for (let i = 0; i < genres.length; i++) {
        const genre = genres[i];
        const play = plays[i];
        
        if (!(genre in genresObj)) {
            genresObj[genre] = [];
            playObj[genre] = 0;
        }
        
        genresObj[genre].push([i, play]);
        playObj[genre] += play;
    }
    
    const sortedGenres = Object.keys(playObj).sort((a, b) => playObj[b] - playObj[a]);
    
    for (const genre of sortedGenres) {
        const sortedSongs = genresObj[genre].sort((a, b) => a[1] === b[1] ? a[0] - b[0] : b[1] - a[1]);
        
         answer.push(...sortedSongs.slice(0, 2).map((song) => song[0]))
    }
    
   return answer;
}