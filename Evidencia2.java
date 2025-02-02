/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package evidencia2;

/**
 *
 * @author Norbe
 */
import java.util.Scanner;

class Node {
    String data;
    Node left, right;

    Node(String data) {
        this.data = data;
        left = right = null;
    }
}

class NodeTree {
    Node root;

    void insert(String data) {
        if (root == null) {
            root = new Node(data);
        } else {
            insertRecursively(data, root);
        }
    }

    void insertRecursively(String data, Node node) {
        if (data.compareTo(node.data) < 0) {
            if (node.left == null) {
                node.left = new Node(data);
            } else {
                insertRecursively(data, node.left);
            }
        } else if (data.compareTo(node.data) > 0) {
            if (node.right == null) {
                node.right = new Node(data);
            } else {
                insertRecursively(data, node.right);
            }
        }
    }

}

class Tree {
    NodeTree tree;

    Tree() {
        tree = new NodeTree();
    }

    void addArea(String areaName, String[] careers) {
        for (String career : careers) {
            tree.insert(areaName + ":" + career);
        }
    }

    void recommendCareer(boolean likeMath, boolean likeBiology, boolean workUnderPressure) {
        recommendCareerHelper(tree.root, likeMath, likeBiology, workUnderPressure);
    }

    void recommendCareerHelper(Node node, boolean likeMath, boolean likeBiology, boolean workUnderPressure) {
        if (node != null) {
            String[] parts = node.data.split(":");
            String area = parts[0];
            String career = parts[1];
            if (likeMath && area.equals("Ingenieria")) {
                System.out.println(career + " (" + area + ")");
            } else if (likeBiology && (area.equals("Medicina") || area.equals("Agronomia"))) {
                System.out.println(career + " (" + area + ")");
            } else if (likeMath && workUnderPressure && area.equals("Ciencias de la Computacion")) {
                System.out.println(career + " (" + area + ")");
            }
            recommendCareerHelper(node.left, likeMath, likeBiology, workUnderPressure);
            recommendCareerHelper(node.right, likeMath, likeBiology, workUnderPressure);
        }
    }
}

public class Evidencia2 {
    static final String[] AREAS = {"Ingenieria", "Ciencias de la Computacion", "Medicina", "Agronomia"};
    static final String[][] CAREERS = {
            {"Ingenieria de Sistemas", "Ingenieria Electrica", "Ingenieria Civil", "Ingenieria Mecanica", "Ingenieria Quimica"},
            {"Ingenieria de Software", "Seguridad Informatica", "Inteligencia Artificial", "Analisis de Datos", "Diseno de Videojuegos"},
            {"Medicina General", "Cirugia", "Pediatria", "Cardiologia", "Dermatologia"},
            {"Veterinaria", "Ingenieria de Agronomia", "Ingenieria de Alimentos", "Zootecnia", "Agroecologia"}
    };

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int option;
        Tree careerTree = new Tree();

        for (int i = 0; i < AREAS.length; i++) {
            careerTree.addArea(AREAS[i], CAREERS[i]);
        }

        do {
            System.out.println("Menu Principal:");
            System.out.println("1. Recomendar carrera en base a habilidades");
            System.out.println("2. Salir");
            System.out.print("Ingrese una opcion: ");
            option = scanner.nextInt();

            switch (option) {
                case 1 -> recommendCareer(scanner, careerTree);
                case 2 -> System.out.println("Saliendo del programa...");
                default -> System.out.println("Opcion invalida.");
            }
        } while (option != 2);
    }

    static void recommendCareer(Scanner scanner, Tree careerTree) {
        System.out.println("Por favor, responda a las siguientes preguntas (ingrese 'S' para salir en cualquier momento):");

        System.out.print("Le gustan las matematicas? (Y/N/S): ");
        char likeMath = obtainValidResponse(scanner);

        if (likeMath == 'S') {
            System.out.println("Saliendo del programa...");
            return;
        }

        System.out.print("Le interesa la biologia? (Y/N/S): ");
        char likeBiology = obtainValidResponse(scanner);

        if (likeBiology == 'S') {
            System.out.println("Saliendo del programa...");
            return;
        }

        char workUnderPressure = 'N';
        if (likeMath == 'Y') {
            System.out.print("Es bueno trabajando bajo presion? (Y/N/S): ");
            workUnderPressure = obtainValidResponse(scanner);
            if (workUnderPressure == 'S') {
                System.out.println("Saliendo del programa...");
                return;
            }
        }

        System.out.print("Tiene habilidades de comunicacion desarrolladas? (Y/N/S): ");
        char goodCommunication = obtainValidResponse(scanner);

        if (goodCommunication == 'S') {
            System.out.println("Saliendo del programa...");
            return;
        }

        System.out.println("\nBasado en sus respuestas, le recomendamos las siguientes carreras:");
        careerTree.recommendCareer(likeMath == 'Y', likeBiology == 'Y', workUnderPressure == 'Y');
    }

    static char obtainValidResponse(Scanner scanner) {
        char response;
        do {
            response = scanner.next().toUpperCase().charAt(0);
            if (response != 'Y' && response != 'N' && response != 'S') {
                System.out.println("Por favor, elija una opcion valida (Y/N/S).");
            }
        } while (response != 'Y' && response != 'N' && response != 'S');
        return response;
    }
}
