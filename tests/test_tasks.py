import unittest
from tasks import agregar_tarea, completar_tarea, pendientes

class TestTasks(unittest.TestCase):
  def test_agregar_tarea(self):
    tareas = []
    tarea = agregar_tarea(tareas, "Leer documentación", "Aprendizaje")
    self.assertEqual(tarea["titulo"], "Leer documentación")
    self.assertEqual(tarea["categoria"], "Aprendizaje")
    self.assertFalse(tarea["completada"])

  def test_agregar_tarea_categoria_vacia(self):
    tareas = []
    with self.assertRaises(ValueError):
      agregar_tarea(tareas, "Leer documentación", "   ")
    
  def test_completar_tarea(self):
    tareas = []
    agregar_tarea(tareas, "Practicar", "Aprendizaje")
    completar_tarea(tareas, 1)
    self.assertEqual(pendientes(tareas), [])

  def test_pendientes_filtra_por_categoria(self):
    tareas = []
    agregar_tarea(tareas, "Practicar Python", "Aprendizaje")
    agregar_tarea(tareas, "Comprar café", "Hogar")
    agregar_tarea(tareas, "Repasar tests", "aprendizaje")
    completar_tarea(tareas, 3)
    filtradas = pendientes(tareas, "aPrEnDiZaJe")
    self.assertEqual(len(filtradas), 1)
    self.assertEqual(filtradas[0]["titulo"], "Practicar Python")
    
if __name__ == "__main__":
  unittest.main()
