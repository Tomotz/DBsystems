function get_templates(){
    var templates = [];
    templates.push($.get("view1/view1.html"));
    templates.push($.get("view2/view2.html"));
    return templates;
}
