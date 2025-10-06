public class WRM {
    Patient dh;
    Patient tail;
    
    public WRM() {
        dh = new Patient(null, null, null, null, null, null);
        dh.next = dh;
        dh.prev = dh;
        tail = dh;
        
    }

    public void registerPatient(int id, String name, int age, String bloodgroup) {
        Patient pat = new Patient(id, name, age, bloodgroup,null,null);
        tail.next= pat;
        pat.prev= tail;
        tail = pat;
        pat.next=dh;
        System.out.println("Success registering patient");
        
    }

    public void servePatient() {
      Patient serve = dh.next;
      Patient pred = serve.prev;
      Patient succ = serve.next;
      String name =(String)serve.name;
      pred.next=succ;
      succ.prev=pred;
      serve.next=null;
      serve.prev=null;
      System.out.println(name +" is served");
        
    }

    public void showAllPatient() {
        Patient current = dh.next;
        if(current==dh){
          System.out.println("No patient in the wrm");
        }
        else{
        while(current!=dh){
          System.out.print(current.name+" ");
          current=current.next;
        }
        System.out.println();
        }
    }

    public boolean canDoctorGoHome() {
       Patient current = dh;
       if(dh==dh.next){
         return true;
       }
       else{
        return false;
       }
    }

    public void cancelAll() {
        dh.next=dh;
        dh.prev=dh;
        System.out.println("All appointments cancelled");
    }


    public void reverseTheLine() {
      Patient f = dh.next;
      Patient l = dh.prev;
      Patient num = dh.next;
      int size = 0;
      int val = 0;
      while(num!=dh){
        size++;
        num=num.next;
      }
      while(val<size){
        Patient temp = f.next;
        temp.prev=f.prev;
        f.prev.next=temp;
        f.next=l.next;
        f.prev=l;
        f.next.prev=f;
        f.prev.next=f;
        f=temp;
        val++;
      } 
      System.out.println("Successfully reversed the line");
                             
      
    }

}
