from sqlalchemy.orm import Session

from core.db.models import Detection


def save_detection(db: Session, detection: Detection):
    detection_item = Detection(
        detection
    )
    # Сохранение информации о детекции в базу данных
    db.add(detection_item)
    db.commit()
