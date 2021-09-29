import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OsppService {


  readonly APIUrl = 'http://127.0.0.1:8000';
  readonly PhotoUrl = 'http://127.0.0.1:8000/media/';

  constructor(private http: HttpClient) { }

  getGruList(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/group/');
  }

  addGroup(val: any) {
    return this.http.post(this.APIUrl + '/group/', val);
  }

  updateGroup(val: any) {
    return this.http.put(this.APIUrl + '/group/', val);
  }

  deleteGroup(val: any) {
    return this.http.delete(this.APIUrl + '/group/' + val);
  }


  getCusList(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/customer/');
  }

  addCustomer(val: any) {
    return this.http.post(this.APIUrl + '/customer/', val);
  }

  updateCustomer(val: any) {
    return this.http.put(this.APIUrl + '/customer/', val);
  }

  deleteCustomer(val: any) {
    return this.http.delete(this.APIUrl + '/customer/' + val);
  }

  UploadPhoto(val: any) {
    return this.http.post(this.APIUrl + '/SaveFile/', val);
  }

  getAllGroupNames(): Observable<any[]> {
    return this.http.get<any[]>(this.APIUrl + '/group/');
  }


}
