// more pseudo-code than actual code
// add same class to parent and all children elements

function setItemNode(node) {
    var child = node.childNodes;
    // foreach or for...in?
    for (var x = 0; x < childNodes.length; x++) {
        // child should hit the sibling and recursively call function until all divs are hit
        if (child[x].childNodes) {
            setItemNode(child[x]);
        }
        
    }
}

