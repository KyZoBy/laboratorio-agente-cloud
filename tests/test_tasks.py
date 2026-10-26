import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes

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

  def test_eliminar_tarea_id_existente(self):
    tareas = []
    agregar_tarea(tareas, "Tarea 1", "General")
    agregar_tarea(tareas, "Tarea 2", "General")
    eliminar_tarea(tareas, 1)
    self.assertEqual(len(tareas), 1)
    self.assertEqual(tareas[0]["id"], 2)

  def test_eliminar_tarea_id_inexistente(self):
    tareas = []
    agregar_tarea(tareas, "Tarea 1", "General")
    with self.assertRaises(ValueError):
      eliminar_tarea(tareas, 99)

  def test_agregar_tarea_no_repite_ids_despues_de_eliminar(self):
    tareas = []
    agregar_tarea(tareas, "Tarea 1", "General")
    agregar_tarea(tareas, "Tarea 2", "General")
    agregar_tarea(tareas, "Tarea 3", "General")
    eliminar_tarea(tareas, 2)
    nueva_tarea = agregar_tarea(tareas, "Tarea 4", "General")
    self.assertEqual(nueva_tarea["id"], 4)
    self.assertEqual([t["id"] for t in tareas], [1, 3, 4])

  def test_pendientes_filtra_por_categoria(self):
    tareas = []
    agregar_tarea(tareas, "Practicar Python", "Aprendizaje")
    agregar_tarea(tareas, "Comprar café", "Hogar")
    agregar_tarea(tareas, "Repasar tests", "aprendizaje")
    completar_tarea(tareas, 3)
    filtradas = pendientes(tareas, "aPrEnDiZaJe")
    self.assertEqual(len(filtradas), 1)
    self.assertEqual(filtradas[0]["titulo"], "Practicar Python")

  def test_pendientes_categoria_inexistente_devuelve_vacia(self):
    tareas = []
    agregar_tarea(tareas, "Practicar Python", "Aprendizaje")
    agregar_tarea(tareas, "Comprar café", "Hogar")
    filtradas = pendientes(tareas, "Trabajo")
    self.assertEqual(filtradas, [])
    
if __name__ == "__main__":
  unittest.main()
