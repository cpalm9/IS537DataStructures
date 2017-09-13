// more pseudo-code than actual code
// add same class to parent and all children elements

function setItemNode(node) {
    x.addClass("class")
    // foreach or for...in?
    for (x in node) {
        // child should hit the sibling and recursively call function until all divs are hit
        if (x.child) {
            setItemNode(child);
        }
        
    }
}

