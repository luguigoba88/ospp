import { Component, OnInit } from '@angular/core';
import {OsppService} from '../../../ospp.service';


@Component({
  selector: 'app-show-cus',
  templateUrl: './show-cus.component.html',
  styleUrls: ['./show-cus.component.scss']
})
export class ShowCusComponent implements OnInit {

  constructor(private service: OsppService) { }

  CustomerList: any = [];

  ModalTitle: string;
  ActivateAddEditCusComp: boolean = false;
  cus: any;

  ngOnInit(): void {
    this.refreshCusList();
  }

  addClick() {
    this.cus = {
      CustomerId: 0,
      CustomerName: '',
      CustomerName2: '',
      CustomerName3: '',
      Surname: '',
      LastName: '',
      DateOfJoining: '',
      Street: '',
      Number: '',
      Suburb: '',
      ZipCode: '',
      PhotoFileName: 'anonymous.png',
      Status: '',
      StatusBC: '',
      StatusWL: '',
      StatusPLD: ''
    };
    this.ModalTitle = 'Agregar Cliente / Prospecto';
    this.ActivateAddEditCusComp = true;

  }

  editClick(item) {
    console.log(item);
    this.cus = item;
    this.ModalTitle = 'Editar Prospecto / Cliente';
    this.ActivateAddEditCusComp = true;
  }

  deleteClick(item) {
    if (confirm('Are you sure??')) {
      this.service.deleteCustomer(item.CustomerId).subscribe(data => {
        alert(data.toString());
        this.refreshCusList();
      });
    }
  }

  closeClick() {
    this.ActivateAddEditCusComp = false;
    this.refreshCusList();
  }


  refreshCusList() {
    this.service.getCusList().subscribe(data => {
      this.CustomerList = data;
    });
  }

}
