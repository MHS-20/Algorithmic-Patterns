class Solution {
    public boolean isBalanced(TreeNode root) {
        return checkHeight(root) != -1;
    }

    private int checkHeight(TreeNode node) {
        if (node == null) return 0;

        int left = checkHeight(node.left);
        if (left == -1) return -1; // sottoalbero sinistro sbilanciato

        int right = checkHeight(node.right);
        if (right == -1) return -1; // sottoalbero destro sbilanciato

        if (Math.abs(left - right) > 1) return -1; // nodo corrente sbilanciato

        return 1 + Math.max(left, right); // ritorna l’altezza
    }
}

