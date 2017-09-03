var movies = [
    {
        title: "the mask",
        rating: "3.8 stars",
        watched: false
    },
    {
        title: "baby driver",
        rating: "4.8 stars",
        watched: false
    },
    {
        title: "the god father",
        rating: "4.6 stars",
        watched: false
    }
];
movies.forEach(function (t) {
    console.log("You have " + (t.watched === true ? "watched " : "not seen " )+ "\"" + t.title + "\"" + " - " + t.rating)
});