function Node(val) {
    this.data = val;
    this.next = null;
}

function Sll() {
    this.head = [{ data: 5, next:{ data: 7, next: { data: 9, next: null } }}];
}

list = new Sll();
    list.add_front = function (val) {

        if (!this.head) {
            this.head = new Node(val);
            return this;
        }

        var temp = this.head;
        this.head = new Node(val);
        this.head.next = temp;
    };

    list.remove_back = function () {

        if (!this.head) {
            return 'nothing to remove';
        }

        var current = this.head;
        var previous = current;
        while (current.next) {
            previous = current;
            current = current.next;
        }
        previous.next = null;
        return this
    };

console.log(Sll(5));