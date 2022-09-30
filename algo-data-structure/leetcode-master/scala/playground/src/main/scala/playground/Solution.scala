package playground

class SingleLinkedNode(_value: Int = -1, _next: SingleLinkedNode = null) {
  var value: Int = _value
  var next: SingleLinkedNode = _next
}
// Definition for singly-linked list.
class MyLinkedList() {

  val dummyHead: SingleLinkedNode = new SingleLinkedNode()
  var size = 0

  def get(index: Int): Int = {
    if (index < 0 || index >= size) return -1

    var i = 0
    var p = dummyHead.next
    while (p != null && i < index) {
      p = p.next
      i += 1
    }

    if (p != null && i == index) p.value
    else -1
  }

  def addAtHead(value: Int): Unit = {
    val newNode = new SingleLinkedNode(value)
    val firstNode = dummyHead.next

    dummyHead.next = newNode
    newNode.next = firstNode
    size += 1
  }

  def addAtTail(value: Int): Unit = {
    val newNode = new SingleLinkedNode(value)

    var prev = dummyHead
    while (prev.next != null) {
      prev = prev.next
    }

    prev.next = newNode
    size += 1
  }

  def addAtIndex(index: Int, value: Int): Unit = {
    if (index < 0 || index > size) return

    val newNode = new SingleLinkedNode(value)

    var prev = dummyHead
    var curr = dummyHead.next
    var i = 0

    while (curr != null && i < index) {
      curr = curr.next
      prev = prev.next
      i += 1
    }

    if (i == index) {
      prev.next = newNode
      newNode.next = curr
      size += 1
    }
  }

  def deleteAtIndex(index: Int): Unit = {
    if (index < 0 || index >= size) return

    var prev = dummyHead
    var curr = dummyHead.next
    var i = 0

    while (curr != null && i < index) {
      curr = curr.next
      prev = prev.next
      i += 1
    }

    if (i == index && curr != null) {
      prev.next = curr.next
      size -= 1
    }
  }

}