import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const roomArray = [];

  roomArray.push(new ClassRoom(19));
  roomArray.push(new ClassRoom(20));
  roomArray.push(new ClassRoom(34));

  return roomArray;
}
